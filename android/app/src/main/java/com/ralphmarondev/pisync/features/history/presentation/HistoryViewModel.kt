package com.ralphmarondev.pisync.features.history.presentation

import android.util.Log
import androidx.compose.runtime.mutableStateListOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.domain.model.Room
import com.ralphmarondev.pisync.core.domain.usecases.GetAllRoomsUseCase
import com.ralphmarondev.pisync.features.history.domain.model.History
import com.ralphmarondev.pisync.features.history.domain.usecases.GetHistoryByRoomIdUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class HistoryViewModel(
    private val getHistoryByRoomIdUseCase: GetHistoryByRoomIdUseCase,
    private val getAllRoomsUseCase: GetAllRoomsUseCase
) : ViewModel() {
    private val _history = MutableStateFlow<List<History>>(emptyList())
    val history = _history.asStateFlow()

    private val _isLoading = MutableStateFlow(false)
    val isLoading = _isLoading.asStateFlow()

    private val _rooms = MutableStateFlow<List<Room>>(emptyList())

    init {
        fetchRooms()
    }

    private fun fetchRooms() {
        viewModelScope.launch {
            try {
                val roomList = getAllRoomsUseCase()
                _rooms.value = roomList

                if (roomList.isNotEmpty()) {
                    fetchHistoryForAllRooms(roomList)
                }
            } catch (e: Exception) {
                Log.e("App", "Error fetching rooms: ${e.message}")
            }
        }
    }

    private fun fetchHistoryForAllRooms(roomList: List<Room>) {
        viewModelScope.launch {
            _isLoading.value = true

            try {
                val histories = mutableStateListOf<History>()

                for (room in roomList) {
                    val historyList = getHistoryByRoomIdUseCase(room.roomId)
                    histories.addAll(historyList)
                }
                _history.value = histories.sortedByDescending { it.timestamp }
            } catch (e: Exception) {
                Log.e("App", "Error fetching history: ${e.message}")
            } finally {
                _isLoading.value = false
            }
        }
    }

    fun refresh() {
        Log.d("App", "Refreshing history list...")
        fetchRooms()
    }
}