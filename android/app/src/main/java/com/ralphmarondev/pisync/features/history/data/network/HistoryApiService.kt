package com.ralphmarondev.pisync.features.history.data.network

import com.ralphmarondev.pisync.features.history.data.model.HistoryDto
import retrofit2.http.GET
import retrofit2.http.Path

interface HistoryApiService {

    @GET("history/room/{id}/")
    suspend fun getHistoryByRoomId(
        @Path("id") id: Int
    ): List<HistoryDto>
}