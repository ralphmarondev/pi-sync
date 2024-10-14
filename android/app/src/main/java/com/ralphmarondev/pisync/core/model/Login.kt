package com.ralphmarondev.pisync.core.model

data class LoginRequest(
    val username: String,
    val password: String
)

data class LoginResponse(
    val token: String
)