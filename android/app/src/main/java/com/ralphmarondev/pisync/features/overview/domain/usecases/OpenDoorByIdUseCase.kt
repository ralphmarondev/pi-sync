package com.ralphmarondev.pisync.features.overview.domain.usecases

import com.ralphmarondev.pisync.features.overview.domain.repositories.OverviewRepository

class OpenDoorByIdUseCase(
    private val repository: OverviewRepository
) {
    suspend operator fun invoke(id: Int, username: String) = repository.openDoorById(id, username)
}