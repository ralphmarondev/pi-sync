package com.ralphmarondev.pisync.features.privacy.data.model

import com.ralphmarondev.pisync.features.privacy.domain.model.Door

data class DoorListResponse(
    val success: Boolean,
    val message: String,
    val doors: List<Door>
)
