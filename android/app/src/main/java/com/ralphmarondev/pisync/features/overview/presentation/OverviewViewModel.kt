package com.ralphmarondev.pisync.features.overview.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.data.local.preferences.AppPreferences
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import com.ralphmarondev.pisync.features.overview.domain.usecases.CloseDoorByIdUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetDoorsByUsernameUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetUserDetailByUsernameUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.OpenDoorByIdUseCase
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.isActive
import kotlinx.coroutines.launch

class OverviewViewModel(
    private val preferences: AppPreferences,
    private val getDoorsByUsernameUseCase: GetDoorsByUsernameUseCase,
    private val closeDoorByIdUseCase: CloseDoorByIdUseCase,
    private val openDoorByIdUseCase: OpenDoorByIdUseCase,
    private val getUserDetailByUsernameUseCase: GetUserDetailByUsernameUseCase
) : ViewModel() {

    private val _fullName = MutableStateFlow("")
    val fullName = _fullName.asStateFlow()

    private val _email = MutableStateFlow("")
    val email = _email.asStateFlow()

    private val _image = MutableStateFlow<String?>(null)
    val image = _image.asStateFlow()

    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors = _doors.asStateFlow()

    private val _isLoading = MutableStateFlow(true)
    val isLoading = _isLoading.asStateFlow()

    private val _username = MutableStateFlow<String?>(null)

    init {
        viewModelScope.launch {
            _isLoading.value = true
            _username.value = preferences.getCurrentUser()
            Log.d("App", "OverviewViewModel, current username: ${_username.value}")

            if (_username.value == null) {
                _isLoading.value = false
                return@launch
            }

            val userDetail = getUserDetailByUsernameUseCase(
                username = _username.value ?: "No username provided"
            )
            _fullName.value = "${userDetail.firstName} ${userDetail.lastName}"
            _email.value = userDetail.email.ifEmpty { _username.value ?: "No username proved" }
            _image.value = userDetail.image

            fetchUpdatesContinuously()
        }
    }

    private fun fetchUpdatesContinuously() {
        viewModelScope.launch {
            while (isActive) {
                try {
                    val updatedDoors = getDoorsByUsernameUseCase(
                        username = _username.value ?: "No username provided."
                    )
                    _doors.value = updatedDoors
                    Log.d("App", "Update door status: ${updatedDoors.map { it.status }}")
                } catch (e: Exception) {
                    Log.e("App", "Failed to fetch doors: ${e.message}")
                }
                _isLoading.value = false
                delay(3000)
            }
        }
    }

    fun setDoorStatus(id: Int) {
        viewModelScope.launch {
            val door = _doors.value.find { it.id == id } ?: return@launch

            if (door.status) {
                closeDoorByIdUseCase(id = id, username = _username.value ?: "No username provided.")
            } else {
                openDoorByIdUseCase(id = id, username = _username.value ?: "No username provided.")
            }

            _doors.value = _doors.value.map {
                if (it.id == id) it.copy(status = !it.status) else it
            }
        }
    }
}