package com.ralphmarondev.pisync.features.home.data.repository

import com.ralphmarondev.pisync.core.data.network.ApiService
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import com.ralphmarondev.pisync.features.home.domain.repository.DoorRepository

class DoorRepositoryImpl(
    private val api: ApiService
) : DoorRepository {
    override suspend fun openDoor(request: DoorActionRequest): DoorActionResponse {
        return api.openDoor(request.doorId, request)
    }

    override suspend fun closeDoor(request: DoorActionRequest): DoorActionResponse {
        return api.closeDoor(request.doorId, request)
    }

    override suspend fun getDoorStatus(id: Int): DoorActionResponse {
        return api.doorStatus(id)
    }
}