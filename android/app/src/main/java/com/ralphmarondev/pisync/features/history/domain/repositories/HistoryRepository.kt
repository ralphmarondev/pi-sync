package com.ralphmarondev.pisync.features.history.domain.repositories

import com.ralphmarondev.pisync.features.history.domain.model.History

interface HistoryRepository {
    suspend fun getHistoryByRoomId(id: Int): List<History>
}