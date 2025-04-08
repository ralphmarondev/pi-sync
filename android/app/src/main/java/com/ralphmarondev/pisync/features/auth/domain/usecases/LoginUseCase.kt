package com.ralphmarondev.pisync.features.auth.domain.usecases

import com.ralphmarondev.pisync.features.auth.domain.repositories.AuthRepository

class LoginUseCase(
    private val repository: AuthRepository
) {
    suspend operator fun invoke(
        username: String,
        password: String
    ): Boolean {
        return repository.login(username, password)
    }
}