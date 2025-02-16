package com.ralphmarondev.pisync.features.history.data.repository

import com.ralphmarondev.pisync.core.data.network.ApiService
import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import com.ralphmarondev.pisync.features.history.domain.repository.DoorLogRepository

class DoorLogRepositoryImpl(
    private val apiService: ApiService
) : DoorLogRepository {
    override suspend fun getDoorLogs(): List<DoorLog> {
        return apiService.getHistory().map { doorLogDto ->
            DoorLog(
                id = doorLogDto.id,
                roomName = doorLogDto.roomName ?: "Unknown Room",
                username = doorLogDto.username,
                description = doorLogDto.description,
                timestamp = doorLogDto.timestamp,
                room = doorLogDto.room
            )
        }
    }
}