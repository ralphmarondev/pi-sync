package com.ralphmarondev.pisync.features.history.domain.usecases

import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import com.ralphmarondev.pisync.features.history.domain.repository.DoorLogRepository

class GetDoorLogsUseCase(
    private val repository: DoorLogRepository
) {
    suspend operator fun invoke(): List<DoorLog> {
        return repository.getDoorLogs()
    }
}