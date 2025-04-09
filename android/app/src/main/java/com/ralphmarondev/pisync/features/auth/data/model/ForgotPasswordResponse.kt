package com.ralphmarondev.pisync.features.auth.domain.model

data class ForgotPasswordResponse(
    val status: Boolean,
    val password_hint: String
)
