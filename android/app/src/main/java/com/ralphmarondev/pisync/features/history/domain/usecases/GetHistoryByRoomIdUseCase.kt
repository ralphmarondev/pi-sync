package com.ralphmarondev.pisync.features.history.domain.usecases

import com.ralphmarondev.pisync.features.history.domain.model.History
import com.ralphmarondev.pisync.features.history.domain.repositories.HistoryRepository

class GetHistoryByRoomIdUseCase(
    private val repository: HistoryRepository
) {
    suspend operator fun invoke(id: Int): List<History> {
        return repository.getHistoryByRoomId(id)
    }
}