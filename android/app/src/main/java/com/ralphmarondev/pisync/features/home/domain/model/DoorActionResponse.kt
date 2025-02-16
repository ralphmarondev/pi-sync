package com.ralphmarondev.pisync.features.home.domain.model

data class DoorActionResponse(
    val success: Boolean,
    val message: String,
    val isOpen: Boolean
)