package com.ralphmarondev.pisync.features.history.presentation

import androidx.lifecycle.ViewModel
import com.ralphmarondev.pisync.features.history.domain.model.History
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class HistoryViewModel : ViewModel() {
    private val _history = MutableStateFlow<List<History>>(emptyList())
    val history = _history.asStateFlow()

    init {
        _history.value += History(
            id = 0,
            roomName = "A14",
            username = "ralphmaron",
            description = "Opened via mobile app",
            timestamp = "",
            room = 0
        )
    }
}