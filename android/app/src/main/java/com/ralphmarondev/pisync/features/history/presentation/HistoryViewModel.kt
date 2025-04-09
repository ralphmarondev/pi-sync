package com.ralphmarondev.pisync.features.history.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.features.history.domain.model.History
import com.ralphmarondev.pisync.features.history.domain.usecases.GetHistoryByRoomIdUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class HistoryViewModel(
    private val getHistoryByRoomIdUseCase: GetHistoryByRoomIdUseCase
) : ViewModel() {
    private val _history = MutableStateFlow<List<History>>(emptyList())
    val history = _history.asStateFlow()

    private val _isLoading = MutableStateFlow(false)
    val isLoading = _isLoading.asStateFlow()

    private val roomId = 1

    init {
        fetchHistory()
    }

    private fun fetchHistory() {
        viewModelScope.launch {
            _isLoading.value = true

            try {
                val historyList = getHistoryByRoomIdUseCase(roomId)
                _history.value = historyList
            } catch (e: Exception) {
                Log.e("App", "Error fetching history: ${e.message}")
            } finally {
                _isLoading.value = false
            }
        }
    }

    fun refresh() {
        Log.d("App", "Refreshing history list...")
        fetchHistory()
    }
}