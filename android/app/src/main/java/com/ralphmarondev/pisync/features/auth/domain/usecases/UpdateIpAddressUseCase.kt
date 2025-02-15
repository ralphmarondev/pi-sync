package com.ralphmarondev.pisync.features.auth.domain.usecases

import com.ralphmarondev.pisync.core.domain.Result
import com.ralphmarondev.pisync.features.auth.domain.repository.AuthRepository

class UpdateIpAddressUseCase(
    private val repository: AuthRepository
) {
    suspend fun invoke(ipAddress: String): Result {
        return try {
            repository.updateIpAddress(ipAddress)
            Result(success = true, message = "Success")
        } catch (e: Exception) {
            Result(success = false, message = e.message)
        }
    }
}