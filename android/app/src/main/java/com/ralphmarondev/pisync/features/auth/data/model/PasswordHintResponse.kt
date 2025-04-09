package com.ralphmarondev.pisync.features.auth.data.model

data class PasswordHintResponse(
    val status: Boolean,
    val message: String,
    val password_hint: String? = null
)
