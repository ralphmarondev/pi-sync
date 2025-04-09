package com.ralphmarondev.pisync.features.history.data.repositories

import com.ralphmarondev.pisync.features.history.data.mapper.toDomain
import com.ralphmarondev.pisync.features.history.data.network.HistoryApiService
import com.ralphmarondev.pisync.features.history.domain.model.History
import com.ralphmarondev.pisync.features.history.domain.repositories.HistoryRepository

class HistoryRepositoryImpl(
    private val api: HistoryApiService
) : HistoryRepository {
    override suspend fun getHistoryByRoomId(id: Int): List<History> {
        return api.getHistoryByRoomId(id).map { it.toDomain() }
    }
}