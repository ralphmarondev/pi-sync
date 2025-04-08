package com.ralphmarondev.pisync.features.overview.domain.usecases

import com.ralphmarondev.pisync.features.overview.domain.repositories.OverviewRepository

class CloseDoorByIdUseCase(
    private val repository: OverviewRepository
) {
    suspend operator fun invoke(id: Int, username: String) = repository.closeDoorById(id, username)
}