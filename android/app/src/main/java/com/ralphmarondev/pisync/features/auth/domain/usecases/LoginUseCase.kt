package com.ralphmarondev.pisync.features.auth.domain.usecases

import android.util.Log
import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.domain.model.User
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class LoginUseCase(private val authRepository: AuthRepository) {
    suspend fun login(user: User): Result {
        return try {
            val loginResponse = authRepository.login(user)
            Log.d("AUTH", "Success: $loginResponse")
            Result(success = true, message = "Login successful.")
        } catch (e: Exception) {
            Log.e("AUTH", "Error: ${e.message}")
            Result(success = false, message = "Login failed.")
        }
    }
}