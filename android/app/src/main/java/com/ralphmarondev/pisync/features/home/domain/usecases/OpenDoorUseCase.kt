package com.ralphmarondev.pisync.features.home.domain.usecases

import com.ralphmarondev.pisync.features.home.domain.model.DoorActionRequest
import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import com.ralphmarondev.pisync.features.home.domain.repository.DoorRepository

class OpenDoorUseCase(
    private val repository: DoorRepository
) {
    suspend operator fun invoke(request: DoorActionRequest): DoorActionResponse {
        return repository.openDoor(request)
    }
}