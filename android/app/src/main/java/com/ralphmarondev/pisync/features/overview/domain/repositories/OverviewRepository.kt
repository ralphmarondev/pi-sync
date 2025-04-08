package com.ralphmarondev.pisync.features.overview.domain.repositories

import com.ralphmarondev.pisync.features.overview.domain.model.Door

interface OverviewRepository {
    suspend fun getDoorsByUsername(username: String): List<Door>

    suspend fun closeDoorById(id: Int, username: String)

    suspend fun openDoorById(id: Int, username: String)
}