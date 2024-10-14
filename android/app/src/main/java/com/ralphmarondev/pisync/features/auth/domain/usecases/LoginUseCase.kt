package com.ralphmarondev.pisync.features.auth.domain.usecases

import android.util.Log
import com.ralphmarondev.pisync.core.model.LoginRequest
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class LoginUseCase(private val authRepository: AuthRepository) {
    suspend fun login(loginRequest: LoginRequest, response: (Boolean, String?) -> Unit) {
        try {
            val loginResponse = authRepository.login(loginRequest)
            Log.d("AUTH", "Success: $loginResponse")
            response(true, loginResponse.token)
        } catch (e: Exception) {
            Log.e("AUTH", "Error: ${e.message}")
            response(false, e.message)
        }
    }
}