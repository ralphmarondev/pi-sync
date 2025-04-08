package com.ralphmarondev.pisync.features.overview.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import com.ralphmarondev.pisync.features.overview.domain.usecases.CloseDoorByIdUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.GetDoorsByUsernameUseCase
import com.ralphmarondev.pisync.features.overview.domain.usecases.OpenDoorByIdUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class OverviewViewModel(
    private val getDoorsByUsernameUseCase: GetDoorsByUsernameUseCase,
    private val closeDoorByIdUseCase: CloseDoorByIdUseCase,
    private val openDoorByIdUseCase: OpenDoorByIdUseCase
) : ViewModel() {
    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors = _doors.asStateFlow()

    private val _isLoading = MutableStateFlow(true)
    val isLoading = _isLoading.asStateFlow()


    init {
        viewModelScope.launch {
            _isLoading.value = true
            val username = "ralphmaron"

            _doors.value = getDoorsByUsernameUseCase(username)
            Log.d("App", "Door status: ${_doors.value[0].status}")
            _isLoading.value = false
        }
    }

    fun setDoorStatus(id: Int) {
        viewModelScope.launch {
            val username = "ralphmaron"

            val door = _doors.value.find { it.id == id } ?: return@launch

            if (door.status) {
                closeDoorByIdUseCase(id, username)
            } else {
                openDoorByIdUseCase(id, username)
            }

            _doors.value = _doors.value.map {
                if (it.id == id) it.copy(status = !it.status) else it
            }
        }
    }
}