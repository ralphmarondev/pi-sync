package com.ralphmarondev.pisync.features.history.data.mapper

import com.ralphmarondev.pisync.features.history.data.model.HistoryDto
import com.ralphmarondev.pisync.features.history.domain.model.History

fun HistoryDto.toDomain(): History {
    return History(
        id = id,
        roomName = roomName,
        username = username,
        description = description,
        timestamp = timestamp,
        roomId = room
    )
}