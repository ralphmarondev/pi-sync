package com.ralphmarondev.pisync.features.auth.domain.usecases

import com.ralphmarondev.pisync.features.auth.domain.repositories.AuthRepository

class ForgotPasswordUseCase(
    private val repository: AuthRepository
) {
    suspend operator fun invoke(username: String): String {
        return repository.getPasswordHint(username = username)
    }
}