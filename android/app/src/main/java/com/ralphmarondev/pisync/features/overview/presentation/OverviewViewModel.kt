package com.ralphmarondev.pisync.features.overview.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class OverviewViewModel : ViewModel() {
    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors = _doors.asStateFlow()

    private val _isLoading = MutableStateFlow(true)
    val isLoading = _isLoading.asStateFlow()


    init {
        viewModelScope.launch {
            _isLoading.value = true

            _doors.value += Door(
                id = 1,
                name = "A14",
                status = false,
                isActive = true
            )
            _doors.value += Door(
                id = 2,
                name = "A15",
                status = true,
                isActive = true
            )
            _isLoading.value = false
        }
    }

    fun setDoorStatus(id: Int) {
        _doors.value = _doors.value.map { door ->
            if (door.id == id) door.copy(status = !door.status) else door
        }
    }
}