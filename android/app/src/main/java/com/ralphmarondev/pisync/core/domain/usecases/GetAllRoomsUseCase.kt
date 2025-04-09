package com.ralphmarondev.pisync.core.domain.usecases

import com.ralphmarondev.pisync.core.domain.model.Room
import com.ralphmarondev.pisync.core.domain.repositories.RoomRepository

class GetAllRoomsUseCase(
    private val repository: RoomRepository
) {
    suspend operator fun invoke(): List<Room> {
        return repository.getAllRooms()
    }
}