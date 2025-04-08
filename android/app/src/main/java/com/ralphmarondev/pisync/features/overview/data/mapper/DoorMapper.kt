package com.ralphmarondev.pisync.features.overview.data.mapper

import com.ralphmarondev.pisync.features.overview.data.models.DoorResponse
import com.ralphmarondev.pisync.features.overview.domain.model.Door

fun DoorResponse.toDomain(): Door {
    return Door(
        id = id,
        name = name,
        status = is_open,
        isActive = is_active
    )
}

fun List<DoorResponse>.toDomain(): List<Door> {
    return this.map { it.toDomain() }
}