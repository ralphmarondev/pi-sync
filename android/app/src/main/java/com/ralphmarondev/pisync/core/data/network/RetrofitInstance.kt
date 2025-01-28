package com.ralphmarondev.pisync.core.data.network

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitInstance {
    private var retrofit: Retrofit? = null
    val api: ApiService
        get() = retrofit?.create(ApiService::class.java)
            ?: throw IllegalStateException("Retrofit is not initialized. Call initialize() first.")

    fun initialize(baseUrl: String) {
        retrofit = Retrofit.Builder()
            .baseUrl(baseUrl)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }
}