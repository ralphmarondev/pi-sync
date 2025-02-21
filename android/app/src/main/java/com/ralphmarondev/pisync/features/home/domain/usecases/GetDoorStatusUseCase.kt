package com.ralphmarondev.pisync.features.home.domain.usecases

import com.ralphmarondev.pisync.features.home.domain.model.DoorActionResponse
import com.ralphmarondev.pisync.features.home.domain.repository.DoorRepository

class GetDoorStatusUseCase(
    private val repository: DoorRepository
) {
    suspend operator fun invoke(id: Int): DoorActionResponse {
        return repository.getDoorStatus(id)
    }
}