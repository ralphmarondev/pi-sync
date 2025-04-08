package com.ralphmarondev.pisync.features.overview.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class OverviewViewModel : ViewModel() {
    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors = _doors.asStateFlow()

    private val _isLoading = MutableStateFlow(true)
    val isLoading = _isLoading.asStateFlow()

    private val _doorStatus = MutableStateFlow(false)
    val doorStatus = _doorStatus.asStateFlow()

    init {
        viewModelScope.launch {
            _isLoading.value = true

            // NOTE: Lets work with one door for now
            _doors.value += Door(
                id = 1,
                name = "A14",
                status = false,
                isActive = true
            )
            _isLoading.value = false
        }
    }

    fun setDoorStatus() {
        _doorStatus.value = !_doorStatus.value
    }
}