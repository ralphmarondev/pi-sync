package com.ralphmarondev.pisync.features.auth.domain.usecases

import android.util.Log
import com.ralphmarondev.pisync.features.auth.domain.model.PasswordHintResponse
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class GetPasswordHintUseCase(
    private val repository: AuthRepository
) {
    suspend operator fun invoke(username: String): PasswordHintResponse {
        return try {
            repository.getPasswordHint(username)
        } catch (e: Exception) {
            Log.e("Auth", "GetPasswordHintUseCase Error: ${e.message}")
            PasswordHintResponse(
                success = false,
                message = e.message ?: "Unknown Error",
                passwordHint = ""
            )
        }
    }
}