package com.ralphmarondev.pisync.core.domain.model

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "rooms")
data class Room(
    @PrimaryKey(autoGenerate = true)
    val id: Int = 0,
    val roomId: Int
)
