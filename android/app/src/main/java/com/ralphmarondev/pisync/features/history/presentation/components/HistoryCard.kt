package com.ralphmarondev.pisync.features.history.presentation.components

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ElevatedCard
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.ralphmarondev.pisync.features.history.domain.model.DoorLog
import java.time.Instant
import java.time.ZoneId
import java.time.format.DateTimeFormatter

@Composable
fun HistoryCard(
    modifier: Modifier = Modifier,
    doorLog: DoorLog,
) {
    ElevatedCard(
        modifier = modifier
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(16.dp)
        ) {
            Text(
                text = doorLog.description,
                fontSize = 16.sp,
                fontWeight = FontWeight.W500,
                color = MaterialTheme.colorScheme.primary
            )
            Text(
                text = "By: ${doorLog.username}",
                fontSize = 16.sp,
                fontWeight = FontWeight.W400,
                color = MaterialTheme.colorScheme.secondary
            )
            Text(
                text = formatTimeStamp(doorLog.timestamp),
                fontSize = 14.sp,
                fontWeight = FontWeight.W300,
                color = MaterialTheme.colorScheme.tertiary
            )
        }
    }
}

private fun formatTimeStamp(timeStamp: String): String {
    val formatter = DateTimeFormatter.ofPattern("hh:mm a • MMMM dd, yyyy")
    val instant = Instant.parse(timeStamp)
    val dateTime = instant.atZone(ZoneId.systemDefault()).toLocalDateTime()
    return dateTime.format(formatter)
}