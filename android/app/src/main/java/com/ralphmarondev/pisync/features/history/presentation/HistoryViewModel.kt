package com.ralphmarondev.pisync.features.history.presentation

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.core.data.network.RetrofitInstance
import com.ralphmarondev.pisync.features.history.data.repository.DoorLogRepositoryImpl
import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import com.ralphmarondev.pisync.features.history.domain.usecases.GetDoorLogsUseCase
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class HistoryViewModel : ViewModel() {
    private val api = RetrofitInstance.api
    private val repository = DoorLogRepositoryImpl(api)
    private val getDoorLogsUseCase = GetDoorLogsUseCase(repository)

    private val _doorLogs = MutableStateFlow<List<DoorLog>>(emptyList())
    val doorLogs: StateFlow<List<DoorLog>> = _doorLogs

    init {
        fetchDoorLogs()
    }

    fun fetchDoorLogs() {
        viewModelScope.launch {
            try {
                _doorLogs.value = getDoorLogsUseCase()
            } catch (e: Exception) {
                Log.e("History", "Error: ${e.message}")
            }
        }
    }
}