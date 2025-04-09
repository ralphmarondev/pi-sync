package com.ralphmarondev.pisync.core.data.repositories

import com.ralphmarondev.pisync.core.data.local.database.dao.RoomDao
import com.ralphmarondev.pisync.core.domain.model.Room
import com.ralphmarondev.pisync.core.domain.repositories.RoomRepository

class RoomRepositoryImpl(
    private val roomDao: RoomDao
) : RoomRepository {

    override suspend fun getAllRooms(): List<Room> {
        return roomDao.getAllRooms()
    }

    override suspend fun saveRoom(room: Room) {
        roomDao.insertRoom(room)
    }

    override suspend fun deleteAllRooms() {
        roomDao.deleteAllRooms()
    }
}