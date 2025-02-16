package com.ralphmarondev.pisync.features.home.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.MyApp
import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.features.home.data.repository.DoorRepositoryImpl
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import com.ralphmarondev.pisync.features.home.domain.usecases.CloseDoorUseCase
import com.ralphmarondev.pisync.features.home.domain.usecases.OpenDoorUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

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

    init {
        viewModelScope.launch {
            _currentUser.value = preferences.getActiveUserUsername() ?: "Invalid User!"
        }
    }

    fun toggleDoorState(
        onResult: (DoorActionResponse) -> Unit
    ) {
        val description = if (_doorState.value) {
            "Opened via mobile app."
        } else {
            "Closed via mobile app."
        }

        val request = DoorActionRequest(
            doorId = 1,
            description = description,
            username = _currentUser.value
        )

        viewModelScope.launch {
            val response = if (_doorState.value) {
                closeDoorUseCase(request)
            } else {
                openDoorUseCase(request)
            }

            onResult(response)
            _doorState.value = !_doorState.value
        }
    }
}