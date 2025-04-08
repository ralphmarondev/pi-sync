package com.ralphmarondev.pisync.features.history.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.history.domain.model.History
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class HistoryViewModel : ViewModel() {
    private val _history = MutableStateFlow<List<History>>(emptyList())
    val history = _history.asStateFlow()

    private val _isLoading = MutableStateFlow(false)
    val isLoading = _isLoading.asStateFlow()

    init {
        viewModelScope.launch {
            _isLoading.value = true
            delay(2000)
            _history.value += History(
                id = 0,
                roomName = "A14",
                username = "ralphmaron",
                description = "Opened via mobile app",
                timestamp = "",
                room = 0
            )
            _isLoading.value = false
        }
    }

    fun refresh() {
        viewModelScope.launch {
            Log.d("App", "Refreshing history list...")
        }
    }
}