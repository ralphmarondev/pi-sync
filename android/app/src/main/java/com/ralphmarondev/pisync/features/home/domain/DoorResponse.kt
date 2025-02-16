package com.ralphmarondev.pisync.features.home.domain

data class DoorResponse(
    val success: Boolean,
    val message: String,
    val is_open: Boolean
)