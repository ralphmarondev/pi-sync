package com.ralphmarondev.pisync.features.auth.domain.model

import com.google.gson.annotations.SerializedName

data class PasswordHintResponse(
    val success: Boolean,
    val message: String,
    @SerializedName("password_hint")
    val passwordHint: String
)