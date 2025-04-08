package com.ralphmarondev.pisync.features.auth.domain.repositories

interface AuthRepository {
    suspend fun login(username: String, password: String): Boolean
}