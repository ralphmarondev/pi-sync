package com.ralphmarondev.pisync.features.overview.domain.usecases

import com.ralphmarondev.pisync.features.overview.domain.repositories.OverviewRepository

class GetDoorsByUsernameUseCase(
    private val repository: OverviewRepository
) {
    suspend operator fun invoke(username: String) = repository.getDoorsByUsername(username)
}