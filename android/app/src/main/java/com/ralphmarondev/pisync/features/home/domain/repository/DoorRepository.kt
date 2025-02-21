package com.ralphmarondev.pisync.features.home.domain.repository

import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse

interface DoorRepository {
    suspend fun openDoor(request: DoorActionRequest): DoorActionResponse
    suspend fun closeDoor(request: DoorActionRequest): DoorActionResponse
    suspend fun getDoorStatus(id: Int): DoorActionResponse
}