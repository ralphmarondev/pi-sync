package com.ralphmarondev.pisync.core.domain.repositories

import com.ralphmarondev.pisync.core.domain.model.Room

interface RoomRepository {
    suspend fun getAllRooms(): List<Room>
    suspend fun saveRoom(room: Room)
    suspend fun deleteAllRooms()
}