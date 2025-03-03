package com.ralphmarondev.pisync.features.home.presentation

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.viewmodel.compose.viewModel
import com.ralphmarondev.pisync.features.home.presentation.components.DoorList
import com.ralphmarondev.pisync.features.home.presentation.components.GreetingsCard
import com.ralphmarondev.pisync.features.home.presentation.components.HomeTopBar

@Composable
fun HomeScreen(
    darkTheme: Boolean,
    toggleDarkTheme: () -> Unit
) {
    val viewModel: HomeViewModel = viewModel()
    val user by viewModel.user.collectAsState()

    Scaffold(
        topBar = {
            HomeTopBar(
                darkTheme = darkTheme,
                toggleDarkTheme = toggleDarkTheme
            )
        }
    ) { innerPadding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding)
        ) {

            user?.let { u ->
                GreetingsCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp),
                    fullName = "${u.firstName} ${u.lastName}",
                    role = if (u.isSuperuser) "Superuser" else "User"
                )
            } ?: run {
                GreetingsCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp),
                    fullName = "Loading...",
                    role = "Loading..."
                )
            }

            Text(
                text = "Registered doors",
                fontSize = 18.sp,
                textAlign = TextAlign.Center,
                fontWeight = FontWeight.W500,
                color = MaterialTheme.colorScheme.secondary,
                modifier = Modifier.padding(horizontal = 16.dp),
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )

            DoorList(viewModel = viewModel)
        }
    }
}