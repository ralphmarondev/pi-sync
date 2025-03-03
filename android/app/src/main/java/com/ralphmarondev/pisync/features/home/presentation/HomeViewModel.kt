package com.ralphmarondev.pisync.features.home.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.MyApp
import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.features.home.data.repository.DoorRepositoryImpl
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import com.ralphmarondev.pisync.features.home.domain.model.User
import com.ralphmarondev.pisync.features.home.domain.model.UserResponse
import com.ralphmarondev.pisync.features.home.domain.usecases.CloseDoorUseCase
import com.ralphmarondev.pisync.features.home.domain.usecases.OpenDoorUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import retrofit2.Response

/* TODO:
    - Get doors registered to the current user.
    - Implement closing and opening door connected to the API.
    - Right now we assume that only one door is assigned to every person.
 */
class HomeViewModel : ViewModel() {
    private val preferences = MyApp.preferences
    private val api = RetrofitInstance.api
    private val repository = DoorRepositoryImpl(api)
    private val openDoorUseCase = OpenDoorUseCase(repository)
    private val closeDoorUseCase = CloseDoorUseCase(repository)

    private val _currentUser = MutableStateFlow("")
    val username: StateFlow<String> get() = _currentUser

    // TODO: get the state from api
    private val _doorState = MutableStateFlow(false)
    val doorState: StateFlow<Boolean> get() = _doorState

    private val _user = MutableStateFlow<User?>(null)
    val user: StateFlow<User?> get() = _user

    init {
        viewModelScope.launch {
            Log.d("Home", "Getting current active user's username...")
            _currentUser.value = preferences.getActiveUserUsername() ?: "Invalid User!"
            Log.d("Home", "Current User: `${_currentUser.value}`")

            Log.d("Home", "Getting user details...")
            Log.d("Home", "Getting registered doors to user: `${_currentUser.value}`...")
            Log.d("Home", "Getting state of registered doors...")
//            _doorState.value = getDoorStatusUseCase(1).isOpen
            Log.d("Home", "Door state: ${_doorState.value}")
            fetchUserDetails(_currentUser.value)
        }
    }

    private suspend fun fetchUserDetails(username: String) {
        try{
            val response: Response<UserResponse> = api.getUserByUsername(username)
            if(response.isSuccessful){
                _user.value = response.body()?.user
                Log.d("Home", "User details fetched successfully!")
            }else{
                Log.e("Home", "Error fetching user details: ${response.code()}")
            }
        }catch (e: Exception){
            Log.e("Home", "Error fetching user details: ${e.message}")
        }
    }

    fun toggleDoorState(
        onResult: (DoorActionResponse) -> Unit
    ) {
        viewModelScope.launch {
            val description = if (!_doorState.value) {
                "Opened via mobile app."
            } else {
                "Closed via mobile app."
            }

            val request = DoorActionRequest(
                doorId = 1,
                description = description,
                username = _currentUser.value
            )

            val response = if (_doorState.value) {
                Log.d("Home", "Closing door.")
                closeDoorUseCase(request)
            } else {
                Log.d("Home", "Opening door.")
                openDoorUseCase(request)
            }

            onResult(response)
            _doorState.value = !_doorState.value
        }
    }
}