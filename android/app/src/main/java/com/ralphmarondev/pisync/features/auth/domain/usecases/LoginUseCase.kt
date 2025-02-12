package com.ralphmarondev.pisync.features.auth.domain.usecases

import android.util.Log
import com.ralphmarondev.pisync.core.data.model.Result
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class LoginUseCase(private val authRepository: AuthRepository) {
    suspend fun login(loginRequest: LoginRequest): Result {
        return try {
            val loginResponse = authRepository.login(loginRequest)
            Log.d("AUTH", "Success: $loginResponse")
            Result(true, "Login successful.")
        } catch (e: Exception) {
            Log.e("AUTH", "Error: ${e.message}")
            Result(false, "Login failed.")
        }
    }
}