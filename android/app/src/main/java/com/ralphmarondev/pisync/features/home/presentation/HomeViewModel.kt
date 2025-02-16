package com.ralphmarondev.pisync.features.home.presentation

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ralphmarondev.pisync.MyApp
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

/* TODO:
    - Get doors registered to the current user.
    - Implement closing and opening door connected to the API.
    - Right now we assume that only one door is assigned to every person.
 */
class HomeViewModel : ViewModel() {
    private val preferences = MyApp.preferences

    private val _currentUser = MutableStateFlow("")
    val username: StateFlow<String> get() = _currentUser

    private val _doorState = MutableStateFlow(false)
    val doorState: StateFlow<Boolean> get() = _doorState

    init {
        viewModelScope.launch {
            _currentUser.value = preferences.getActiveUserUsername() ?: "Invalid User!"
        }
    }

    fun toggleDoorState() {
        _doorState.value = !_doorState.value
    }
}