package com.ralphmarondev.pisync.features.history.domain.repository

import com.ralphmarondev.pisync.features.history.domain.model.DoorLog

interface DoorLogRepository {
    suspend fun getDoorLogs(): List<DoorLog>
}