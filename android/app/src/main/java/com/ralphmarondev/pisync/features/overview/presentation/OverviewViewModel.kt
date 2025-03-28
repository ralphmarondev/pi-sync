package com.ralphmarondev.pisync.features.overview.presentation

import androidx.lifecycle.ViewModel
import com.ralphmarondev.pisync.features.overview.domain.model.Door
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class OverviewViewModel : ViewModel() {
    private val _doors = MutableStateFlow<List<Door>>(emptyList())
    val doors = _doors.asStateFlow()

    init {
        _doors.value += Door(
            id = 1,
            name = "A14",
            status = false,
            isActive = true
        )

        _doors.value += Door(
            id = 2,
            name = "A16",
            status = true,
            isActive = true
        )

        // TODO: Every 3 seconds read the status of doors from db and update
    }
}