package com.ralphmarondev.pisync.features.overview.data.models

data class DoorListResponse(
    val success: Boolean,
    val message: String,
    val doors: List<DoorResponse>
)
