package com.ralphmarondev.pisync.features.home.presentation.components

import android.widget.Toast
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import com.ralphmarondev.pisync.features.home.presentation.HomeViewModel

@Composable
fun DoorList(
    modifier: Modifier = Modifier,
    viewModel: HomeViewModel
) {
    val context = LocalContext.current
    val doorState by viewModel.doorState.collectAsState()

    val door by viewModel.door.collectAsState()


    LazyVerticalGrid(
        modifier = modifier
            .fillMaxWidth(),
        columns = GridCells.Fixed(2),
        horizontalArrangement = Arrangement.spacedBy(8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp),
        contentPadding = PaddingValues(horizontal = 16.dp, vertical = 8.dp)
    ) {
        item {
            DoorCard(
                checked = doorState,
                toggleChecked = {
                    viewModel.toggleDoorState { response ->
                        if (response.success) {
                            Toast.makeText(context, response.message, Toast.LENGTH_SHORT)
                                .show()
                        } else {
                            Toast.makeText(
                                context,
                                "Failed to toggle door.",
                                Toast.LENGTH_SHORT
                            ).show()
                        }
                    }
                },
                label = "Door: $door",
                modifier = Modifier
                    .fillMaxWidth()
            )
        }
    }
}