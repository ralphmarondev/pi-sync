package com.ralphmarondev.pisync.features.home.presentation

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow

class HomeViewModel : ViewModel() {
    private val _selectedIndex = MutableStateFlow(0)
    val selectedIndex = _selectedIndex.asStateFlow()

    fun onSelectedIndexValueChange(value: Int) {
        _selectedIndex.value = value
    }
}